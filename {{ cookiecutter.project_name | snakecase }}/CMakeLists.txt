cmake_minimum_required(VERSION 3.16)
project({{ cookiecutter.project_name | snakecase }} CXX)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Werror -Wall -Wextra -Wpedantic -Wshadow
    -Wsign-conversion -Winit-self -Wredundant-decls)
endif()

option(BUILD_SHARED_LIBS "Build shared libraries" ON)

set(THIS_PACKAGE_INCLUDE_DEPENDS
  rclcpp
  eigen3_cmake_module
  Eigen3
)

find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()

###########
## Build ##
###########

# Declare a C++ library
add_library(
  ${PROJECT_NAME}
  src/{{ cookiecutter.class_name | snakecase }}.cpp
)
ament_target_dependencies(${PROJECT_NAME} ${THIS_PACKAGE_INCLUDE_DEPENDS})
target_include_directories(${PROJECT_NAME}
  PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
         $<INSTALL_INTERFACE:include>)
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)

# Declare a C++ executable
add_executable(
  ${PROJECT_NAME}_node
  src/main.cpp
)
target_link_libraries(${PROJECT_NAME}_node ${PROJECT_NAME})
ament_target_dependencies(${PROJECT_NAME}_node ${THIS_PACKAGE_INCLUDE_DEPENDS})

#############
## Install ##
#############

install(
  TARGETS ${PROJECT_NAME} ${PROJECT_NAME}_node
  EXPORT ${PROJECT_NAME}Targets
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(PROGRAMS
  nodes/{{cookiecutter.python_node_name}}.py
  DESTINATION lib/${PROJECT_NAME}
)

#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
  find_package(ament_lint_auto REQUIRED)
  find_package(ament_cmake_pytest REQUIRED)

  # ROS2 linters, but disable copyright test. PickNik's copyright's may not conform
  # to this test
  # set(ament_cmake_copyright_FOUND TRUE)
  # ament_lint_auto_find_test_dependencies()

  # GTests
  ament_add_gtest({{ cookiecutter.class_name | snakecase }}_test test/{{ cookiecutter.class_name | snakecase }}_test.cpp)
  target_link_libraries({{ cookiecutter.class_name | snakecase }}_test
    ${PROJECT_NAME})
  ament_target_dependencies({{ cookiecutter.class_name | snakecase }}_test ${THIS_PACKAGE_INCLUDE_DEPENDS})
endif()

ament_export_targets(${PROJECT_NAME}Targets HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_package()
