from itertools import chain, combinations
from graph import generate_random_graph
import math
import subprocess

def power_set(iterable):
    """
    Generate all subsets (power set) of a given iterable.
    """
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def intersection_family_and_set(subset, family) :
    """
    Returns a set of intersection of given set with each set in the 
    family. {S /\ F | for all F in Family}
    """
    # @ToDo - Improve performance using frozensets
    family_intersection_set = []
    for f in family : 
        f_intersection_subset = f.intersection(subset)
        if f_intersection_subset not in family_intersection_set : 
            family_intersection_set.append(f_intersection_subset)
    return family_intersection_set

def compare_family(family1, family2) : 
    """
    Compare two families and returns true if same
    [(1,2), (2)] , [(2,1), (3)]
    """
    for subset in family1 : 
        if set(subset) not in family2 : 
            return False
    return True  

def is_shattered(subset, family):
    """
    Check if a subset is shattered by the family of subsets.
    A subset is shattered if all its subsets appear in the family.
    """
    subset_power_set = power_set(subset)
    family_intersection_set = intersection_family_and_set(subset, family)
    if compare_family(subset_power_set, family_intersection_set) : 
        return True
    return False

def find_largest_shattered_set(universe, family):
    """
    Find the largest shattered set and its size.
    """
    n = len(universe)
    largest_shattered_set = set()
    shattered_set_ub = math.floor(math.log2(n)) + 1
    all_shattered_sets = []

    degree_of_vertices = [len(subset) for subset in family]
    
    # Check all subsets of the universe
    for k in range(shattered_set_ub):  # Iterate through subset sizes
        # print(f"Going through all sets of size {k}")
        for subset in combinations(universe, k):
            # print("Subset to Shatter - ", subset)
            # Skip the set if degree bound is not met
            degree_of_subset = [degree_of_vertices[i - 1] for i in subset]
            degree_bound_violated = False
            for deg in degree_of_subset : 
                if k > deg :
                    degree_bound_violated = True 
                    break
            if (degree_bound_violated) :
                continue

            if is_shattered(set(subset), family):
                all_shattered_sets.append(set(subset))
                if len(subset) > len(largest_shattered_set):
                    largest_shattered_set = set(subset)
    
    return largest_shattered_set, len(largest_shattered_set), all_shattered_sets

def compute_vc_dimension(n, family):
    """
    Compute the VC dimension of a given universe and family.
    """
    universe = set(range(1, n + 1))
    family = [set(f) for f in family]  # Convert family to a list of sets
    largest_shattered_set, size, all_shattered_sets = find_largest_shattered_set(universe, family)
    return largest_shattered_set, size, all_shattered_sets

def print_all_shattered_sets() : 
    family =[{1,2,3}, {2,4,5,1}, {3,6,7,1}, {4,2, 8}, {5,2}, {6,3}, {7,3}, {8,4}]
    largest_shattered_set, size, all_shattered_sets = compute_vc_dimension(8, family)
    for subset in all_shattered_sets: 
        print(subset)


# Main 
if __name__ == "__main__":
    # All Shattered sets
    print_all_shattered_sets()


def experiment_bad_algo_vs_inria() : 
    n = 50
    # for i in range(100) : # no of iterations
    family, filename = generate_random_graph(n) 
    degree_of_vertices = [len(subset) for subset in family]
    log_degree_of_vertices = [math.floor(math.log2(degree)) + 1 for degree in degree_of_vertices]
    shattered_set, vc_dimension, all_shattered_sets = compute_vc_dimension(n, family)
    # print(f'Graph : {family}')
    print(f"Largest Shattered Set: {shattered_set}")
    print(f"VC Dimension: {vc_dimension}")
    # print("Shattered Sets")
    # for s in all_shattered_sets : 
    #     print(s)
    print("#####################")
    print("                     ")
    # run_inria_algo(filename)

def experiment_degree_and_shattered_set_size() :
    for n in range(1, 1000) :  
        for i in range(2000) : 
            family = generate_random_graph(n)
            degree_of_vertices = [len(subset) for subset in family]
            log_degree_of_vertices = [math.floor(math.log2(degree)) + 1 for degree in degree_of_vertices]
            shattered_set, vc_dimension, all_shattered_sets = compute_vc_dimension(n, family)
            # print('#####')
            # print(f'Graph : {family}')
            # print(f"Largest Shattered Set: {shattered_set}")
            # print(f"VC Dimension: {vc_dimension}")
            # print(f"Degree of Vertices: {degree_of_vertices}")
            # print(f"Log Degree + 1 of Vertices: {log_degree_of_vertices}")
            for subset in all_shattered_sets:
                if len(subset) > 0:
                    min_log_degree_of_vertex = min(log_degree_of_vertices[v - 1] for v in subset)
                    if len(subset) > min_log_degree_of_vertex : 
                        print("********** Found **********")
                        print(f"{subset} - Counter Example")
                        print("********** Found **********")
                        print(f'Graph : {family}')
                        print(f"Largest Shattered Set: {shattered_set}")
                        print(f"VC Dimension: {vc_dimension}")
                        print(f"Degree of Vertices: {degree_of_vertices}")
                        print(f"Log Degree + 1 of Vertices: {log_degree_of_vertices}")
        print(f"No Counter Examples for vertex size {n}")


def run_inria_algo(filename) : 
    print("Running Inria Algo")
    command = f"./_build/main vcdim {filename}"

    try:
        # Run the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
        # Print errors if any
        if result.stderr:
            print("Command Errors:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print(f"Error Output: {e.stderr}")


# [{1, 3, 5, 8, 9}, {2, 3, 5, 6, 7, 8, 9, 10}, {1, 2, 3, 5, 10}, {8, 4, 6, 7},
# {1, 2, 3, 5, 9, 10}, {2, 4, 6, 7, 8, 10}, {2, 4, 6, 7, 8, 9, 10}, {1, 2, 4, 6, 7, 8},
# {1, 2, 5, 7, 9}, {2, 3, 5, 6, 7, 10}]

# {7, 9, 10 } trace = [ {7}, {9}, {10}, {9,10}, {7, 10}, , {7,9}, {7,9,10}]


### New Algo 
# 1. Run from 1 to log n only 
# 2. Make a binary search on VC Dimension - (Later)
# 3. If Found a shattered set 
# 3.1 Remove all the vertices of degree lesser than size of the shattered set 
# 4. Continue the process until - Shattered Set = universe
# Time Complexity - 

# Based on degree we can eliminate many vertices 
# 1. Find VC dimension as below
# 2. Choose a number k - denoting vc dimension. |Z| <= deg(v)
# 3. Remove all the vertices with degree < k from the Universe 
# 4. Find a shattered set -> If found then update value of k as per binary search 
# 5. If not found then decrease the value of vc dimension.

# Subroutine - Find a shattered sets - n^k 
# Properties related to degree