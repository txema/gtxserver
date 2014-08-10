
South
-----

    Setting up a legacy project and database
        1 - add south to installed apps
        2 - run syncdb, this will add the south tables to the database
        3 - for each of your apps run python manage.py schemamigration app_name --initial This will create your initial migrations
        4 - for each of your apps run python manage.py migrate app_name 0001 --fake , this will fake out south,
            it won't do anything to the database for those models, it will just add records to the south_migrationhistory table
            so that the next time you want to create a migration, you are all set.

     Setting up a legacy project and no database
        1 - create database
        2 - add south to installed apps
        3 - for each of your apps run python manage.py schemamigration app_name --initial This will create your initial migrations
        4 - run python manage.py syncdb, this will add any apps that don't have migrations to the database
        5 - then run south migrate python manage.py migrate this will run all migrations for your apps.


GIT
---






