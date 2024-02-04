import os
from bottle import run, request, get, app
from bottle_cors_plugin import cors_plugin

steel_map = {
  "1.4116": {
    "toughness": 2.5,
    "edge_retention": 2.5,
    "corrosion_resistance": 8.0
  },
  "14C28N": {
    "toughness": 9.0,
    "edge_retention": 3.0,
    "corrosion_resistance": 8.5
  },
  "154CM": {
    "toughness": 3.5,
    "edge_retention": 4.5,
    "corrosion_resistance": 7.0
  },
  "420HC": {
    "toughness": 9.0,
    "edge_retention": 2.5,
    "corrosion_resistance": 8.0
  },
  "440A": {
    "toughness": 3.5,
    "edge_retention": 3.5,
    "corrosion_resistance": 8.5
  },
  "440C": {
    "toughness": 3.5,
    "edge_retention": 4.5,
    "corrosion_resistance": 7.5
  },
  "AEB-L": {
    "toughness": 9.0,
    "edge_retention": 3.0,
    "corrosion_resistance": 7.0
  },
  "AUS-8/8Cr13MoV": {
    "toughness": 6.0,
    "edge_retention": 3.0,
    "corrosion_resistance": 7.0
  },
  "BDIN": {
    "toughness": 3.5,
    "edge_retention": 3.5,
    "corrosion_resistance": 8.5
  },
  "CPM-154": {
    "toughness": 5.0,
    "edge_retention": 4.5,
    "corrosion_resistance": 7.0
  },
  "Elmax": {
    "toughness": 4.0,
    "edge_retention": 5.5,
    "corrosion_resistance": 8.0
  },
  "LC200N": {
    "toughness": 8.5,
    "edge_retention": 3.0,
    "corrosion_resistance": 10.0
  },
  "M390/20CV/204P": {
    "toughness": 3.5,
    "edge_retention": 6.5,
    "corrosion_resistance": 9.0
  },
  "M398": {
    "toughness": 2.5,
    "edge_retention": 9.0,
    "corrosion_resistance": 8.0
  },
  "MagnaCut": {
    "toughness": 7.0,
    "edge_retention": 5.0,
    "corrosion_resistance": 9.5
  },
  "N690": {
    "toughness": 3.5,
    "edge_retention": 4.5,
    "corrosion_resistance": 8.0
  },
  "Nitro-V": {
    "toughness": 7.5,
    "edge_retention": 3.0,
    "corrosion_resistance": 7.0
  },
  "S110V": {
    "toughness": 3.0,
    "edge_retention": 8.0,
    "corrosion_resistance": 9.0
  },
  "S125V": {
    "toughness": 2.5,
    "edge_retention": 9.5,
    "corrosion_resistance": 7.5
  },
  "S30V": {
    "toughness": 4.0,
    "edge_retention": 6.0,
    "corrosion_resistance": 7.5
  },
    "S35VN": {
    "toughness": 5.0,
    "edge_retention": 5.0,
    "corrosion_resistance": 7.5
  },
  "S45VN": {
    "toughness": 4.0,
    "edge_retention": 5.5,
    "corrosion_resistance": 8.0
  },
  "S60V": {
    "toughness": 3.5,
    "edge_retention": 7.0,
    "corrosion_resistance": 7.0
  },
  "S90V": {
    "toughness": 3.5,
    "edge_retention": 9.0,
    "corrosion_resistance": 7.5
  },
  "Super Gold 2": {
    "toughness": 4.0,
    "edge_retention": 5.0,
    "corrosion_resistance": 7.5
  },
  "Vanax": {
    "toughness": 5.0,
    "edge_retention": 5.5,
    "corrosion_resistance": 10.0
  },
  "VG10": {
    "toughness": 4.0,
    "edge_retention": 4.5,
    "corrosion_resistance": 7.5
  },
  "XHP": {
    "toughness": 5.0,
    "edge_retention": 5.5,
    "corrosion_resistance": 6.5
  }
}

@get('/')
def query():
  if "priorities" in request.params:
    priorities_param = request.params.priorities.split(",")
    max_weighted_sum = float('-inf')
    max_steel = ""
    for steel, properties in steel_map.items():
      properties["weighted_sum"] = sum([v * float(priorities_param[i]) for i, (k, v) in enumerate(properties.items()) if k != "weighted_sum"])
      if properties["weighted_sum"] > max_weighted_sum:
        max_weighted_sum = properties["weighted_sum"]
        max_steel = steel
    return { max_steel: steel_map[max_steel] }
  else:
    return { "error": "steel parameter is empty."}

app = app()
app.install(cors_plugin('*'))

port = int(os.environ.get('PORT', 4000))
run(host='0.0.0.0', port=port, debug=True)

