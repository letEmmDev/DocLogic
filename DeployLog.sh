Finished
Deployed in 21 seconds

Created: 49 seconds ago

Deployment Logs
Updating nginx configuration is enabled for this application
Updating the doclogic.applikuapp.com subdomain configuration
ran run_deployment_v3 for deployment 163655
??? Connecting to app@13.39.190.144:22
YML configuration file is not used.
Escaping for env var values is enabled for this application.
Writing env/envs_export.sh to disk...
Writing env/dot.env to disk...
 * Running deployment script:

Deployment 163655
Storing private ssh key
done
Cloning...
Cloning into 'doclogic/code'...

...Cloning done
git STATUS:
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
COMMIT_INFO:71b641c Project fix - Settings for deployment on Appliku v3


Size of the cloned code directory:
7.0M	doclogic/code
Writing dockerfile to disk...done.
Writing docker-compose.yml to disk...done.
Building image...

Writing commit info: 71b641c Project fix - Settings for deployment on Appliku v3
 Image doclogic_one_off:163655 Building 
 Image doclogic_web:163655 Building 

#1 [internal] load local bake definitions

#1 reading from stdin 899B done
#1 DONE 0.0s

#2 [one_off internal] load build definition from Dockerfile
#2 transferring dockerfile: 1.03kB done

#2 DONE 0.0s

#3 [web internal] load metadata for docker.io/library/python:3.11.9-bullseye

#3 DONE 0.6s

#4 [web internal] load .dockerignore
#4 transferring context: 2B done
#4 DONE 0.0s

#5 [web  1/11] FROM docker.io/library/python:3.11.9-bullseye@sha256:64da8e5fd98057b05db01b49289b774e9fa3b81e87b4883079f6c31fb141b252
#5 resolve docker.io/library/python:3.11.9-bullseye@sha256:64da8e5fd98057b05db01b49289b774e9fa3b81e87b4883079f6c31fb141b252 0.0s done
#5 DONE 0.0s

#6 [web internal] load build context

#6 transferring context: 6.71MB 0.1s done
#6 DONE 0.1s

#7 [web  2/11] RUN apt-get update  && apt-get install -y --force-yes  nano python3-pip gettext chrpath libssl-dev libxft-dev  libfreetype6 libfreetype6-dev  libfontconfig1 libfontconfig1-dev && rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [web  3/11] RUN pip install --upgrade pip && pip install gunicorn
#8 CACHED

#9 [web  4/11] WORKDIR /code/
#9 CACHED

#10 [web  5/11] COPY ./code/requirements.txt /code/
#10 CACHED

#11 [web  6/11] RUN pip install -r requirements.txt
#11 CACHED

#12 [one_off  7/11] COPY ./code/ /code/

#12 DONE 0.1s

#13 [one_off  8/11] COPY ./env/ /env/
#13 DONE 0.1s

#14 [web  9/11] RUN source /env/envs_export.sh && if [ -n "$BUILD_COMMAND" ]; then eval $BUILD_COMMAND; fi

#14 DONE 0.3s

#15 [web 10/11] RUN source /env/envs_export.sh && if [ -f "manage.py" ]; then if [ "$DISABLE_COLLECTSTATIC" == "1" ]; then echo "collect static disabled"; else echo "Found manage.py, running collectstatic" && python manage.py collectstatic --noinput; fi;  else echo "No manage.py found. Skipping collectstatic."; fi;

#15 0.235 Found manage.py, running collectstatic

#15 1.017 
#15 1.017 197 static files copied to '/code/staticfiles'.

#15 DONE 1.2s

#16 [one_off 11/11] RUN useradd -ms /bin/bash code

#16 DONE 0.4s

#17 [one_off] exporting to image
#17 exporting layers

#17 exporting layers 0.6s done

#17 exporting manifest sha256:e1b3c8f222a800251e39a729f25cb46e48a45db03cf82be5bf66e37a19b109c7 0.0s done
#17 exporting config sha256:5f394d84626442f0a20288ca6b4af2427727b092417c700ccd5bd0d4d4874291 0.0s done
#17 exporting attestation manifest sha256:0b3551da74a392db654aad995619d22bcc8109acca6be9023543d476cf0e2514

#17 exporting attestation manifest sha256:0b3551da74a392db654aad995619d22bcc8109acca6be9023543d476cf0e2514 0.1s done
#17 exporting manifest list sha256:d628b12dbfcb18e478744db34f818226a8882aacc6eba81f1631d343469f6073 0.0s done
#17 naming to docker.io/library/doclogic_one_off:163655 done
#17 unpacking to docker.io/library/doclogic_one_off:163655

#17 unpacking to docker.io/library/doclogic_one_off:163655 0.4s done

#17 DONE 1.3s

#18 [web] exporting to image
#18 exporting layers 0.6s done
#18 exporting manifest sha256:f8ba0f73a04b217706fe6009d455adabbcba43ab44c12cd1ae58ec61b5735e15 0.0s done
#18 exporting config sha256:2b2903c195e750d934ed57fae583cc7e7ff68f0c054f4d92c87c45e663ce30da 0.0s done
#18 exporting attestation manifest sha256:f1c37a1a62f8dc091ca4c665e7f0e763c33594e112b25c269690794bf02a406c 0.1s done
#18 exporting manifest list sha256:9fbf9e793d3047da218f523c3f56b802b465c13393436872f33cb6ca0ebd6361 0.0s done
#18 naming to docker.io/library/doclogic_web:163655 0.0s done
#18 unpacking to docker.io/library/doclogic_web:163655 0.4s done
#18 DONE 1.3s


#19 [one_off] resolving provenance for metadata file

#19 DONE 0.0s

#20 [web] resolving provenance for metadata file
#20 DONE 0.0s
 Image doclogic_web:163655 Built 
 Image doclogic_one_off:163655 Built 

build_script exit_code: 0
 Container doclogic-one_off-1 Stopping 
 Container doclogic_web Stopping 
 Container doclogic-one_off-run-9fbe2b6f4958 Stopping 
 Container doclogic-one_off-1 Stopped 
 Container doclogic-one_off-1 Removing 
 Container doclogic-one_off-run-9fbe2b6f4958 Stopped 
 Container doclogic-one_off-run-9fbe2b6f4958 Removing 

 Container doclogic_web Stopped 
 Container doclogic_web Removing 
 Container doclogic-one_off-run-9fbe2b6f4958 Removed 
 Container doclogic-one_off-1 Removed 
 Container doclogic_web Removed 
 Container doclogic-one_off-run-9fbe2b6f4958 Stopping 
 Container doclogic-one_off-run-9fbe2b6f4958 Error Error while Stopping
 Container doclogic-one_off-run-9fbe2b6f4958 Removed 

 Container doclogic_web Creating 
 Container doclogic-one_off-1 Creating 

 Container doclogic_web Created 

 Container doclogic-one_off-1 Created 
 Container doclogic_web Starting 
 Container doclogic-one_off-1 Starting 

 Container doclogic_web Started 

 Container doclogic-one_off-1 Started 


deployment_script exit_code: 0
 Container doclogic-one_off-run-c45d40fdd7e7 Creating 

 Container doclogic-one_off-run-c45d40fdd7e7 Created 

Starting release process...

(0.004) 
            SELECT
                c.relname,
                CASE
                    WHEN c.relispartition THEN 'p'
                    WHEN c.relkind IN ('m', 'v') THEN 'v'
                    ELSE 't'
                END,
                obj_description(c.oid, 'pg_class')
            FROM pg_catalog.pg_class c
            LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relkind IN ('f', 'm', 'p', 'r', 'v')
                AND n.nspname NOT IN ('pg_catalog', 'pg_toast')
                AND pg_catalog.pg_table_is_visible(c.oid)
        ; args=None; alias=default

(0.001) SELECT "django_migrations"."id", "django_migrations"."app", "django_migrations"."name", "django_migrations"."applied" FROM "django_migrations"; args=(); alias=default
(0.001) 
            SELECT
                c.relname,
                CASE
                    WHEN c.relispartition THEN 'p'
                    WHEN c.relkind IN ('m', 'v') THEN 'v'
                    ELSE 't'
                END,
                obj_description(c.oid, 'pg_class')
            FROM pg_catalog.pg_class c
            LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relkind IN ('f', 'm', 'p', 'r', 'v')
                AND n.nspname NOT IN ('pg_catalog', 'pg_toast')
                AND pg_catalog.pg_table_is_visible(c.oid)
        ; args=None; alias=default
(0.000) SELECT "django_migrations"."id", "django_migrations"."app", "django_migrations"."name", "django_migrations"."applied" FROM "django_migrations"; args=(); alias=default
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, hospital, patient_management, sessions
Running migrations:
  No migrations to apply.
(0.002) 
            SELECT
                c.relname,
                CASE
                    WHEN c.relispartition THEN 'p'
                    WHEN c.relkind IN ('m', 'v') THEN 'v'
                    ELSE 't'
                END,
                obj_description(c.oid, 'pg_class')
            FROM pg_catalog.pg_class c
            LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relkind IN ('f', 'm', 'p', 'r', 'v')
                AND n.nspname NOT IN ('pg_catalog', 'pg_toast')
                AND pg_catalog.pg_table_is_visible(c.oid)
        ; args=None; alias=default
(0.000) SELECT "django_migrations"."id", "django_migrations"."app", "django_migrations"."name", "django_migrations"."applied" FROM "django_migrations"; args=(); alias=default
(0.001) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_typ
e" WHERE "django_content_type"."app_label" = 'admin'; args=('admin',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'admin' AND "django_content_type"."model" IN ('logentry')); args=('admin', 'logentry'); alias=default
(0.001) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (1) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, 2 ASC; args=(1,); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'admin'; args=('admin',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'auth'; args=('auth',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'auth' AND "django_content_type"."model" IN ('permission', 'group')); args=('auth', 'permission', 'group'); alias=default
(0.001) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (2, 3) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, 2 ASC; args=(2, 3); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE
 "django_content_type"."app_label" = 'auth'; args=('auth',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'contenttypes'; args=('contenttypes',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'contenttypes' AND "django_content_type"."model" IN ('contenttype')); args=('contenttypes', 'contenttype'); alias=default
(0.000) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (4) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, 2 ASC; args=(4,); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'contenttypes'; args=('contenttypes',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'sessions'; args=('sessions',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'sessions' AND "django_content_type"."model" IN ('session')); args=('sessions', 'session'); alias=default
(0.000) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (5) ORDER BY "dja
ngo_content_type"."app_label" ASC, "django_content_type"."model" ASC, 2 ASC; args=(5,); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'sessions'; args=('sessions',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'django_recaptcha'; args=('django_recaptcha',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'django_recaptcha'; args=('django_recaptcha',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'core'; args=('core',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'core' AND "django_content_type"."model" IN ('customuser')); args=('core', 'customuser'); alias=default
(0.000) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (6) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, 2 ASC; args=(6,); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'core'; args=('core',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_t
ype" WHERE "django_content_type"."app_label" = 'hospital'; args=('hospital',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'hospital' AND "django_content_type"."model" IN ('service', 'specialization', 'doctor', 'hospital', 'department')); args=('hospital', 'service', 'specialization', 'doctor', 'hospital', 'department'); alias=default
(0.001) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (7, 8, 9, 10, 11) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, 2 ASC; args=(7, 8, 9, 10, 11); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'hospital'; args=('hospital',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'patient_management'; args=('patient_management',); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."app_label" = 'patient_management' AND "django_content_type"."model" IN ('patient')); args=('patient_management', 'patient'); alias=default
(0.000) SELECT "auth_permission"."content_type_id" AS "content_type", "auth_permission"."codename" AS "codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (12) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."mod
el" ASC, 2 ASC; args=(12,); alias=default
(0.000) SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'patient_management'; args=('patient_management',); alias=default

(0.004) 
            SELECT
                c.relname,
                CASE
                    WHEN c.relispartition THEN 'p'
                    WHEN c.relkind IN ('m', 'v') THEN 'v'
                    ELSE 't'
                END,
                obj_description(c.oid, 'pg_class')
            FROM pg_catalog.pg_class c
            LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relkind IN ('f', 'm', 'p', 'r', 'v')
                AND n.nspname NOT IN ('pg_catalog', 'pg_toast')
                AND pg_catalog.pg_table_is_visible(c.oid)
        ; args=None; alias=default

(0.001) SELECT "django_migrations"."id", "django_migrations"."app", "django_migrations"."name", "django_migrations"."applied" FROM "django_migrations"; args=(); alias=default
(0.001) SELECT "core_customuser"."last_login", "core_customuser"."is_superuser", "core_customuser"."id_user", "core_customuser"."name", "core_customuser"."surname", "core_customuser"."email", "core_customuser"."password", "core_customuser"."role", "core_customuser"."date_joined", "core_customuser"."is_active", "core_customuser"."is_staff", "core_customuser"."is_patient", "core_customuser"."is_admin" FROM "core_customuser" WHERE "core_customuser"."email" = 'superdoctor@doclogic.com' LIMIT 21; args=('superdoctor@doclogic.com',); alias=default

(0.003) INSERT INTO "core_customuser" ("last_login", "is_superuser", "name", "surname", "email", "password", "role", "date_joined", "is_active", "is_staff", "is_patient", "is_admin") VALUES (NULL, true, NULL, NULL, 'superdoctor@doclogic.com', 'pbkdf2_sha256$1000000$sHaTv2DmBQ597Y6dAsoWSk$X30aC92jg9HW7W9ePuJfXzdV/QFo4RelG+k9nP+jJo4=', 'admin', '2025-12-11T18:10:28.371645+00:00'::timestamptz, true, true, false, false) RETURNING "core_customuser"."id_user"; args=(None, True, None, None, 'superdoctor@doclogic.com', 'pbkdf2_sha256$1000000$sHaTv2DmBQ597Y6dAsoWSk$X30aC92jg9HW7W9ePuJfXzdV/QFo4RelG+k9nP+jJo4=', 'admin', datetime.datetime(2025, 12, 11, 18, 10, 28, 371645, tzinfo=datetime.timezone.utc), True, True, False, False); alias=default

Superuser created successfully.

Release process finished.


release_script exit_code: 0

Connection closed to the server. Exit code: 0
Deployment finished with exit_code: 0