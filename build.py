#!/usr/bin/env python3

#
# Copyright 2023 Two Six Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Script to build yaml-cpp for RACE
"""

import logging
import os
import race_ext_builder as builder


def get_cli_arguments():
    """Parse command-line arguments to the script"""
    parser = builder.get_arg_parser("yaml-cpp", "0.6.2", 1, __file__)
    return builder.normalize_args(parser.parse_args())


if __name__ == "__main__":
    args = get_cli_arguments()
    builder.make_dirs(args)
    builder.setup_logger(args)

    builder.fetch_source(
        args=args,
        source=f"https://github.com/jbeder/yaml-cpp/archive/refs/tags/yaml-cpp-{args.version}.tar.gz",
        extract="tar.gz",
    )

    source_dir = os.path.join(args.source_dir, f"yaml-cpp-yaml-cpp-{args.version}")
    env = builder.create_standard_envvars(args)

    logging.root.info("Configuring build")
    if args.target.startswith("linux"):
        builder.execute(args, [
            "cmake",
            f"-H{source_dir}",
            f"-B{args.build_dir}",
            f"-DCMAKE_STAGING_PREFIX={args.install_dir}",
            f"-DCMAKE_INSTALL_PREFIX={args.install_prefix}",
            "-DBUILD_SHARED_LIBS=ON",
        ], env=env)

    elif args.target.startswith("android"):
        builder.execute(args, [
            "cmake",
            f"-H{source_dir}",
            f"-B{args.build_dir}",
            f"-DCMAKE_STAGING_PREFIX={args.install_dir}",
            f"-DCMAKE_INSTALL_PREFIX={args.install_prefix}",
            f"-DCMAKE_TOOLCHAIN_FILE={os.environ['ANDROID_NDK']}/{args.target}.toolchain.cmake",
            "-DBUILD_SHARED_LIBS=ON",
            "-DYAML_CPP_BUILD_TESTS=OFF",
        ])

    logging.root.info("Building")
    builder.execute(args, [
        "cmake",
        "--build",
        args.build_dir,
        "--target",
        "install",
        "--",
        "-j",
        args.num_threads,
    ])

    builder.create_package(args)
