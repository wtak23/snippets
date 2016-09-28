import json
import plotly
import os

# load global schema files
schema_path = os.path.join(plotly.__path__[0],'graph_reference/default-schema.json')
with open(schema_path, 'r') as f:
     data = json.load(f)
     
cwd = os.path.dirname(__file__)
#%% 
data.keys()

data_defs = data['defs']
data_traces = data['traces']
data_layout = data['layout']['layoutAttributes']

# dump setup
setup = dict(indent=2,)
#%% === create defs schema ===
with open(os.path.join(cwd,'defs-schema.json'),'w') as f:
    json.dump(data_defs,f,**setup)
#%% create output dump dir for these HUGE json files
traces_dir = os.path.join(cwd,'traces')
layout_dir = os.path.join(cwd,'layout')

if not os.path.isdir(traces_dir):
    os.makedirs(traces_dir)

if not os.path.isdir(layout_dir):
    os.makedirs(layout_dir)
#%% dump attributes for each trace object in json format
for key in data_traces.keys():
    #print ' {} '.format(key).center(50,'=')
    #print json.dumps(data_traces[key],indent=2)
    outfile = os.path.join(traces_dir,key+'.json')
    with open(outfile,'w') as f:
        json.dump(data_traces[key],f,**setup)
#%% repeat for layoout objects
for key in data_layout.keys():
    outfile = os.path.join(layout_dir,key+'.json')
    with open(outfile,'w') as f:
        json.dump(data_layout[key],f,**setup)