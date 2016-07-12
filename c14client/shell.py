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

from c14 import C14
from c14client import parser
from c14client import utils

import os


def protocol(c14api):
    """Handle protocols related actions."""

    data = [['name', []],
            ['description', []]]

    protocols = c14api.list_protocols()
    for protocol in protocols:
        data[0][1].append(protocol['name'])
        data[1][1].append(protocol['description'])
    utils.output_informations(data)


def platform(c14api, options):
    """Handle platforms related actions."""

    if options.action == 'get':
        platform = c14api.get_platform(options.id)
        data = [['id', [platform['id']]],
                ['$ref', [platform['$ref']]]]
        utils.output_informations(data)

    elif options.action == 'list':
        data = [['id', []],
                ['$ref', []]]
        platforms = c14api.list_platforms()
        for platform in platforms:
            data[0][1].append(platform['id'])
            data[1][1].append(platform['$ref'])
        utils.output_informations(data)


def archive(c14api, options):
    """Handle archives related actions."""

    if options.action == 'create':
        id = c14api.create_archive(options.safe_id, options.name,
                                   options.description, options.protocols,
                                   options.platforms, options.parity,
                                   options.ssh_keys, options.days)
        if isinstance(id, dict):
            print(id)
        else:
            data = [['name', [options.name]],
                    ['uuid', [id]],
                    ['status', ['active']],
                    ['description', [options.description]]]
            utils.output_informations(data)

    elif options.action == 'get':
        archive = c14api.get_archive(options.safe_id, options.uuid)
        data = [['name', [archive['name']]],
                ['uuid', [archive['uuid_ref']]],
                ['status', [archive['status']]],
                ['description', [archive['description']]],
                ['$ref', [archive['$ref']]]]
        utils.output_informations(data)

    elif options.action == 'list':
        data = [['name', []],
                ['uuid', []],
                ['status', []],
                ['$ref', []]]
        archives = c14api.list_archives(options.safe_id)
        for archive in archives:
            data[0][1].append(archive['name'])
            data[1][1].append(archive['uuid_ref'])
            data[2][1].append(archive['status'])
            data[3][1].append(archive['$ref'])
        utils.output_informations(data)

    elif options.action == 'update':
        res = c14api.update_archive(options.safe_id, options.uuid,
                                    options.name, options.description)
        if isinstance(res, dict):
            print(res)
        else:
            print('Archive updated')

    elif options.action == 'delete':
        archive = c14api.get_archive(options.safe_id, options.uuid)
        res = c14api.delete_archive(options.safe_id, options.uuid)
        if isinstance(res, dict):
            print(res)
        else:
            data = [['name', [archive['name']]],
                    ['uuid', [archive['uuid_ref']]],
                    ['status', ['deleting']],
                    ['description', [archive['description']]],
                    ['$ref', [archive['$ref']]]]
            utils.output_informations(data)

    elif options.action == 'archive':
        res = c14api.archive_archive(options.safe_id, options.uuid)
        if isinstance(res, dict):
            print(res)
        else:
            print('Archiving files from temporary storage')

    elif options.action == 'info':
        data = [['login', []],
                ['password', []],
                ['ssh_keys', []],
                ['uri', []],
                ['status', []]]

        info = c14api.archive_informations(options.safe_id, options.uuid)
        for credential in info['credentials']:
            data[0][1].append(credential['login'])
            data[1][1].append(credential['password'])
            if 'ssh_keys' in credential:
                data[2][1].append(credential['ssh_keys'][0]['description'])
            else:
                data[2][1].append(None)
            data[3][1].append(credential['uri'])
            data[4][1].append(info['status'])

        utils.output_informations(data)

    elif options.action == 'job-list':
        data = [['type', []],
                ['status', []],
                ['progress', []],
                ['start', []],
                ['end', []],
                ['uuid', []]]
        jobs = c14api.archive_list_jobs(options.safe_id, options.uuid)
        for job in jobs:
            data[0][1].append(job['type'])
            data[1][1].append(job['status'])
            data[2][1].append(job['progress'])
            data[3][1].append(job['start'])
            data[4][1].append(job['end'])
            data[5][1].append(job['uuid_ref'])
        utils.output_informations(data)

    elif options.action == 'job-info':
        info = c14api.archive_get_job(options.safe_id, options.uuid,
                                      options.job_id)
        data = [['type', [info['type']]],
                ['status', [info['status']]],
                ['progress', [info['progress']]],
                ['start', [info['start']]],
                ['end', [info['end']]],
                ['uuid', [info['uuid_ref']]]]
        utils.output_informations(data)

    elif options.action == 'get-key':
        res = c14api.archive_get_encryption_key(options.safe_id, options.uuid)
        print(res)

    elif options.action == 'set-key':
        res = c14api.archive_set_encryption_key(options.safe_id, options.uuid,
                                                options.key)
        if isinstance(res, dict):
            print(res)
        else:
            print('Key set')

    elif options.action == 'delete-key':
        res = c14api.archive_delete_encryption_key(options.safe_id,
                                                   options.uuid)
        if isinstance(res, dict):
            print(res)
        else:
            print('Key deleted')

    elif options.action == 'location-list':
        data = [['id', []],
                ['$ref', []]]
        locations = c14api.archive_list_locations(options.safe_id,
                                                  options.uuid)
        for location in locations:
            data[0][1].append(location['uuid_ref'])
            data[1][1].append(location['$ref'])
        utils.output_informations(data)

    elif options.action == 'location-info':
        location = c14api.archive_get_location(options.safe_id, options.uuid,
                                               options.location_id)
        data = [['id', [location['uuid_ref']]],
                ['$ref', [location['$ref']]]]
        utils.output_informations(data)

    elif options.action == 'verify':
        location = c14api.verify_archive(options.safe_id, options.uuid,
                                         options.location_id)
        if isinstance(location, dict):
            print(location)
        else:
            print location

    elif options.action == 'unarchive':
        res = c14api.unarchive(options.safe_id, options.uuid,
                               options.location_id, options.protocols)
        if isinstance(res, dict):
            print(res)
        else:
            print('Unarchiving archive')


def safe(c14api, options):
    """Handle safes related actions."""

    if options.action == 'create':
        id = c14api.create_safe(options.name, options.description)
        if isinstance(id, dict):
            print(id)
        else:
            data = [['name', [options.name]],
                    ['uuid', [id]],
                    ['status', ['active']],
                    ['description', [options.description]]]
            utils.output_informations(data)

    elif options.action == 'get':
        safe = c14api.get_safe(options.uuid)
        data = [['name', [safe['name']]],
                ['uuid', [safe['uuid_ref']]],
                ['status', [safe['status']]],
                ['description', [safe['description']]],
                ['$ref', [safe['$ref']]]]
        utils.output_informations(data)

    elif options.action == 'list':
        data = [['name', []],
                ['uuid', []],
                ['status', []],
                ['$ref', []]]
        safes = c14api.list_safes()
        for safe in safes:
            data[0][1].append(safe['name'])
            data[1][1].append(safe['uuid_ref'])
            data[2][1].append(safe['status'])
            data[3][1].append(safe['$ref'])
        utils.output_informations(data)

    elif options.action == 'update':
        res = c14api.update_safe(options.uuid, options.name,
                                 options.description)
        if isinstance(res, dict):
            print(res)

    elif options.action == 'delete':
        res = c14api.delete_safe(options.uuid)
        if isinstance(res, dict):
            print(res)
        else:
            data = [['name', [safe['name']]],
                    ['uuid', [safe['uuid_ref']]],
                    ['status', ['deleting']],
                    ['description', [safe['description']]],
                    ['$ref', [safe['$ref']]]]
            utils.output_informations(data)


def main():

    options = parser.parse()

    if not os.environ.get('C14_TOKEN'):
        print('c14client: Environment variable $C14_TOKEN not found')
    else:
        c14api = C14(os.environ.get('C14_TOKEN'))
        if options.which == 'safe':
            safe(c14api, options)
        elif options.which == 'archive':
            archive(c14api, options)
        elif options.which == 'platform':
            platform(c14api, options)
        elif options.which == 'protocol':
            protocol(c14api)
