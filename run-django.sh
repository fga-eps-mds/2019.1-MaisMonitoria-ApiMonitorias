python3 manage.py makemigrations 

until python3 manage.py migrate; do
  sleep 2
  echo "Retry!";
done

python3 manage.py runserver 0.0.0.0:8001