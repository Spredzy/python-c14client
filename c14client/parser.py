# Copyright 2016 Yanis Guenane <yanis@guenane.org>
# Author: Yanis Guenane <yanis@guenane.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from c14client.version import __version__

import argparse


def parse():

    parser = argparse.ArgumentParser(
        description='Online.net C14 storage solution client',
        argument_default=argparse.SUPPRESS
    )

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__)

    subparsers = parser.add_subparsers(help='commands')

    safe_parser = subparsers.add_parser('safe',
                                        help='Safes related operations')
    safe_parser.set_defaults(which='safe')
    safe_parser.add_argument('action',
                             choices=['create', 'get', 'list', 'update',
                                      'delete'],
                             help='Action to operate on the safe')

    safe_parser.add_argument('--name', help='Name of the safe')
    safe_parser.add_argument('--description', help='Description of the safe')
    safe_parser.add_argument('--uuid', help='UUID of the safe')

    archive_parser = subparsers.add_parser('archive',
                                           help='Archives related operations')
    archive_parser.set_defaults(which='archive')
    archive_parser.add_argument('action',
                                choices=['archive', 'create', 'delete-key',
                                         'get', 'get-key', 'info', 'job-info',
                                         'job-list', 'list', 'location-list',
                                         'location-info', 'set-key', 'verify',
                                         'unarchive', 'update', 'delete'],
                                help='Action to operate on the archive')

    archive_parser.add_argument('--name', help='Name of the archive')
    archive_parser.add_argument('--description',
                                help='Description of the archive')
    archive_parser.add_argument('--uuid',
                                help='UUID of the archive')

    archive_parser.add_argument('--safe-id', help='UUID of the safe')
    archive_parser.add_argument('--job-id', help='UUID of the archive job')
    archive_parser.add_argument('--location-id',
                                help='UUID of the archive location')
    archive_parser.add_argument('--parity',
                                choices=['STANDARD', 'ENTERPRISE'],
                                help='Type of service')
    archive_parser.add_argument('--protocols', action='append',
                                choices=['SSH', 'FTP', 'WebDAV'],
                                help='Protocols the archive will support')
    archive_parser.add_argument('--platforms',
                                action='append', choices=['1', '2'],
                                help='Ids of platforms')
    archive_parser.add_argument('--ssh-keys', help='UUIDs of SSH keys')
    archive_parser.add_argument('--days', type=int,
                                help='Number of days until archive')
    archive_parser.add_argument('--key',
                                help='The encryption key for the archive')

    protocol_parser = subparsers.add_parser('protocol',
                                            help='Protocol related operations')
    protocol_parser.set_defaults(which='protocol')
    protocol_parser.add_argument('action', choices=['list'],
                                 help='Action to operate on the protocol')

    platform_parser = subparsers.add_parser('platform',
                                            help='Platform related operations')
    platform_parser.set_defaults(which='platform')
    platform_parser.add_argument('action', choices=['get', 'list'],
                                 help='Action to operate on the platform')

    platform_parser.add_argument('--id', help='UUID of the platform')

    options = parser.parse_args()

    return options
