The Wealthy Laughing Duck Project
---------------------------------

This repository is a [duck component](https://github.com/wealthy-laughing-duck).
Visit [Wealthy Laughing Duck Project](http://wealthy-laughing-duck.github.io/) for more information.

This repository holds files used among other duck components (fixtures, thrift, etc.)

Fixtures
--------

run fixture generator:

    $ cd fixtures/
    $ ./generate -h
    usage: generate [-h] [-V] format

    positional arguments:
      format         sql or json

    optional arguments:
      -h, --help     show this help message and exit
      -V, --version  show program's version number and exit

generate SQL fixtures:

    $ ./generate sql
    Following files generated successfully:
     - sql/fixtures.sql
     - sql/access.sql

generate JSON fixtures:

    $ ./generate json
    Following files generated successfully:
     - json/category.json
     - json/outcome.json
     - json/users.json
     - json/income.json

Dependencies
------------

Following duck components rely on duck-commons:

 * [duck-rip-api](https://github.com/wealthy-laughing-duck/duck-api-rip) - needs MySQL database to run django api application
 * [wealthy-laughing-duck / original project](https://github.com/wealthy-laughing-duck/wealthy-laughing-duck)- needs MySQL database for Hibernate and optionally thrift to regenerate thrift classes
