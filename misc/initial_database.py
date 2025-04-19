import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://absensi-dbd9d-default-rtdb.firebaseio.com/",
    },
)
# menambahkan data dosen
ref = db.reference("Lecturers")

data = {
    "1023048901": {
        "id": "1023048901",
        "name": "Arbi Haza Nasution",
        "password": "admin",
        "address": "Pekanbaru, Riau",
        "email": "Arbihaza@gmail.com",
        "major": "Ilmu Data",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
