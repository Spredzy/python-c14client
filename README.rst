python-c14client
================

A python client for Online.net C14 storage solution.

**Note**: One needs to export its token to the environment variable ``$C14_TOKEN``.

Usage
-----

Protocol
^^^^^^^^

.. code-block::

    #> c14client protocol list
    +--------+----------------------------------------------------------------+
    |  name  |                          description                           |
    +--------+----------------------------------------------------------------+
    |  SSH   | Transfer files using a secure protocol like SCP, SFTP or RSYNC |
    |  FTP   |                                                                |
    | WEBDAV |         Mount your temporary space on your own device          |
    +--------+----------------------------------------------------------------+
 

Platform
^^^^^^^^

.. code-block::

    #> c14client platform list
    +----+--------------------------------+
    | id |              $ref              |
    +----+--------------------------------+
    | 1  | /api/v1/storage/c14/platform/1 |
    +----+--------------------------------+

    #> c14client platform get --id 1
    +----+--------------------------------+
    | id |              $ref              |
    +----+--------------------------------+
    | 1  | /api/v1/storage/c14/platform/1 |
    +----+--------------------------------+


Safe
^^^^

.. code-block::

  
    #> c14client safe list
    +--------+--------------------------------------+--------+---------------------------------------------------------------+
    |  name  |                 uuid                 | status |                              $ref                             |
    +--------+--------------------------------------+--------+---------------------------------------------------------------+
    | backup | d22d47a4-45e2-11e6-be10-10604b9b0ad9 | active | /api/v1/storage/c14/safe/d20d07a4-45e2-11e6-be10-10604b9b0ad9 |
    +--------+--------------------------------------+--------+---------------------------------------------------------------+

    #> c14client safe get --uuid d22d47a4-45e2-11e6-be10-10604b9b0ad9
    +--------+--------------------------------------+--------+-------------------------------------------+---------------------------------------------------------------+
    |  name  |                 uuid                 | status |                description                |                              $ref                             |
    +--------+--------------------------------------+--------+-------------------------------------------+---------------------------------------------------------------+
    | backup | d22d47a4-45e2-11e6-be10-10604b9b0ad9 | active | Coffre Fort pour mes backups personnelles | /api/v1/storage/c14/safe/d20d07a4-45e2-11e6-be10-10604b9b0ad9 |
    +--------+--------------------------------------+--------+-------------------------------------------+---------------------------------------------------------------+

    #> c14client safe update --uuid d22d47a4-45e2-11e6-be10-10604b9b0ad9 --name 'backup-newname'

    #> c14client safe get --uuid d22d47a4-45e2-11e6-be10-10604b9b0ad9                           
    +----------------+--------------------------------------+--------+-------------------------------------------+---------------------------------------------------------------+
    |  name          |                 uuid                 | status |                description                |                              $ref                             |
    +----------------+--------------------------------------+--------+-------------------------------------------+---------------------------------------------------------------+
    | backup-newname | d22d47a4-45e2-11e6-be10-10604b9b0ad9 | active | Coffre Fort pour mes backups personnelles | /api/v1/storage/c14/safe/d20d07a4-45e2-11e6-be10-10604b9b0ad9 |
    +----------------+--------------------------------------+--------+-------------------------------------------+---------------------------------------------------------------+
 
    #> c14client safe delete --uid xxx
    +----------------+--------------------------------------+----------+-------------------------------------------+---------------------------------------------------------------+
    |  name          |                 uuid                 |  status  |                description                |                              $ref                             |
    +----------------+--------------------------------------+----------+-------------------------------------------+---------------------------------------------------------------+
    | backup-newname | d22d47a4-45e2-11e6-be10-10604b9b0ad9 | deleting | Coffre Fort pour mes backups personnelles | /api/v1/storage/c14/safe/d20d07a4-45e2-11e6-be10-10604b9b0ad9 |
    +----------------+--------------------------------------+----------+-------------------------------------------+---------------------------------------------------------------+


Archive
^^^^^^^

**TODO**: Will provide output example later. Commands are functionals.

.. code-block::

    #> c14client archive list --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9'
    [...]
    #> c14client archive create --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --name 'ANAME' --description 'ADESC' --protocols SSH --protocols FTP --platforms 1
    [...]
    #> c14client archive get --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive update --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID' --name 'anewname'
    [...]
    #> c14client archive delete --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive archive --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive info --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive job-list --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive job-info --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive get-key --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive set-key --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID' --key 'AKEY'
    [...]
    #> c14client archive delete-key --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive location-list --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
    [...]
    #> c14client archive location-info --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID' --location-id 'ALOCATIONID'
    [...]
    #> c14client archive verify --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID' --location-id 'ALOCATIONID'
    [...]
    #> c14client archive unarchive --safe-id 'd22d47a4-45e2-11e6-be10-10604b9b0ad9' --uuid 'ARCHIVEUUID'
