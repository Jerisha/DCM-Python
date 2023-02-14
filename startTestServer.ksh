export ORACLE_HOME=/opt/oracle/product/19.0.0.client
/opt/SP/osnapp/dcmadmin/workspace/dcm/dcmvenv/bin/gunicorn DCM.wsgi --bind 0.0.0.0:5000 --workers 1 --threads 3 --timeout 500