graph = {
    "Cairo": {
        "lat": 30.0444, "lon": 31.2357,
        "neighbors": ["Alexandria", "Aswan", "Luxor", "Giza", "Port Said", "Suez", "Ismailia", "Faiyum", "6th of October City"]
    },
    "Alexandria": {
        "lat": 31.2001, "lon": 29.9187,
        "neighbors": ["Cairo", "Port Said", "Damanhur", "El Alamein", "Marsa Matruh"]
    },
    "Aswan": {
        "lat": 24.0889, "lon": 32.8998,
        "neighbors": ["Cairo", "Luxor", "Edfu", "Kom Ombo"]
    },
    "Luxor": {
        "lat": 25.6872, "lon": 32.6396,
        "neighbors": ["Cairo", "Aswan", "Qena", "Esna"]
    },
    "Giza": {
        "lat": 30.0131, "lon": 31.2089,
        "neighbors": ["Cairo", "Faiyum", "6th of October City"]
    },
    "Port Said": {
        "lat": 31.2653, "lon": 32.3019,
        "neighbors": ["Cairo", "Alexandria", "Ismailia", "Damietta"]
    },
    "Suez": {
        "lat": 29.9737, "lon": 32.5263,
        "neighbors": ["Cairo", "Ismailia", "Hurghada"]
    },
    "Ismailia": {
        "lat": 30.6043, "lon": 32.2723,
        "neighbors": ["Cairo", "Port Said", "Suez"]
    },
    "Faiyum": {
        "lat": 29.3084, "lon": 30.8428,
        "neighbors": ["Cairo", "Giza", "Beni Suef"]
    },
    "6th of October City": {
        "lat": 29.9381, "lon": 30.9138,
        "neighbors": ["Cairo", "Giza"]
    },
    "El Alamein": {"lat":30.8176,"lon":28.945,"neighbors":["Alexandria","Marsa Matruh"]},
    "Marsa Matruh": {"lat":31.3525,"lon":27.2453,"neighbors":["Alexandria","El Alamein","Siwa"]},
    "Edfu": {"lat":24.9785,"lon":32.8758,"neighbors":["Aswan","Luxor","Asyut"]},
    "Kom Ombo": {"lat":24.4525,"lon":32.9282,"neighbors":["Aswan","Edfu"]},
    "Qena": {"lat":26.1615,"lon":32.7181,"neighbors":["Luxor","Sohag","Hurghada"]},
    "Esna": {"lat":25.2934,"lon":32.554,"neighbors":["Luxor","Qena"]},
    "Damietta": {"lat":31.4165,"lon":31.8133,"neighbors":["Port Said","Mansoura"]},
    "Beni Suef": {"lat":29.0744,"lon":31.0979,"neighbors":["Faiyum","Minya"]},
    "Tanta": {"lat":30.7885,"lon":31.0019,"neighbors":["Damanhur","Mansoura","Zagazig"]},
    "Kafr El Sheikh": {"lat":31.1143,"lon":30.9394,"neighbors":["Damanhur","Tanta"]},
    "Asyut": {"lat":27.181,"lon":31.1837,"neighbors":["Edfu","Beni Suef","Sohag"]},
    "Hurghada": {"lat":27.2579,"lon":33.8116,"neighbors":["Suez","Qena","Safaga"]},
    "Mansoura": {"lat":31.0364,"lon":31.3807,"neighbors":["Damietta","Tanta","Zagazig"]},
    "Minya": {"lat":28.1099,"lon":30.7503,"neighbors":["Beni Suef","Asyut","El Minya"]},
    "Zagazig": {"lat":30.5877,"lon":31.502,"neighbors":["Tanta","Mansoura","Ismailia"]},
    "Sohag": {"lat":26.557,"lon":31.6948,"neighbors":["Qena","Asyut","El Balyana"]},
    "Safaga": {"lat":26.7292,"lon":33.9365,"neighbors":["Hurghada","Quseir"]},
    "El Minya": {"lat":28.0916,"lon":30.7522,"neighbors":["Minya","El Balyana","Mallawi"]},
    "El Balyana": {"lat":26.2324,"lon":31.3525,"neighbors":["Sohag","El Minya","Abydos"]},
    "Mallawi": {"lat":27.7314,"lon":30.8416,"neighbors":["El Minya","Asyut","Amarna"]},
    "Quseir": {"lat":26.1046,"lon":34.2778,"neighbors":["Safaga","Marsa Alam"]},
    "Marsa Alam": {"lat":25.0661,"lon":34.8965,"neighbors":["Quseir","Aswan"]},
    "Siwa": {"lat":29.2041,"lon":25.5195,"neighbors":["Marsa Matruh"]},
    "Abydos": {"lat":26.1856,"lon":31.9196,"neighbors":["El Balyana"]},
    "Amarna": {"lat":27.6473,"lon":30.9475,"neighbors":["Mallawi"]},
}
