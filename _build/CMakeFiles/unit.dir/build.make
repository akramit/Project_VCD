# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/amitroy/Documents/GitHub/graph-vcdim

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/amitroy/Documents/GitHub/graph-vcdim/_build

# Include any dependencies generated for this target.
include CMakeFiles/unit.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/unit.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/unit.dir/flags.make

CMakeFiles/unit.dir/src/unit.cc.o: CMakeFiles/unit.dir/flags.make
CMakeFiles/unit.dir/src/unit.cc.o: ../src/unit.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/unit.dir/src/unit.cc.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/unit.dir/src/unit.cc.o -c /home/amitroy/Documents/GitHub/graph-vcdim/src/unit.cc

CMakeFiles/unit.dir/src/unit.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/unit.dir/src/unit.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/amitroy/Documents/GitHub/graph-vcdim/src/unit.cc > CMakeFiles/unit.dir/src/unit.cc.i

CMakeFiles/unit.dir/src/unit.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/unit.dir/src/unit.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/amitroy/Documents/GitHub/graph-vcdim/src/unit.cc -o CMakeFiles/unit.dir/src/unit.cc.s

# Object files for target unit
unit_OBJECTS = \
"CMakeFiles/unit.dir/src/unit.cc.o"

# External object files for target unit
unit_EXTERNAL_OBJECTS = \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/integers.cc.o" \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/distrib.cc.o" \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/index.cc.o" \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/set_system.cc.o" \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/graph.cc.o" \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/partition.cc.o" \
"/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/common.dir/src/vcdim.cc.o"

unit: CMakeFiles/unit.dir/src/unit.cc.o
unit: CMakeFiles/common.dir/src/integers.cc.o
unit: CMakeFiles/common.dir/src/distrib.cc.o
unit: CMakeFiles/common.dir/src/index.cc.o
unit: CMakeFiles/common.dir/src/set_system.cc.o
unit: CMakeFiles/common.dir/src/graph.cc.o
unit: CMakeFiles/common.dir/src/partition.cc.o
unit: CMakeFiles/common.dir/src/vcdim.cc.o
unit: CMakeFiles/unit.dir/build.make
unit: CMakeFiles/unit.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable unit"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/unit.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/unit.dir/build: unit

.PHONY : CMakeFiles/unit.dir/build

CMakeFiles/unit.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/unit.dir/cmake_clean.cmake
.PHONY : CMakeFiles/unit.dir/clean

CMakeFiles/unit.dir/depend:
	cd /home/amitroy/Documents/GitHub/graph-vcdim/_build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/amitroy/Documents/GitHub/graph-vcdim /home/amitroy/Documents/GitHub/graph-vcdim /home/amitroy/Documents/GitHub/graph-vcdim/_build /home/amitroy/Documents/GitHub/graph-vcdim/_build /home/amitroy/Documents/GitHub/graph-vcdim/_build/CMakeFiles/unit.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/unit.dir/depend

