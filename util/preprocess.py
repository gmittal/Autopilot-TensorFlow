# Make Udacity datasets NVIDIA friendly
import os, pandas, sys, tqdm

PATH = sys.argv[1]

# Read a CSV file
data = pandas.read_csv(PATH+'/interpolated.csv')
centered = data[(data['frame_id'] == 'center_camera')].reset_index(drop=True)

with open(PATH + '/data.txt', 'w') as out:
    for i in tqdm.tqdm(range(len(centered['frame_id']))):
        out.write(str(centered['filename'][i]) + ' ' + str(centered['angle'][i]) + '\n')
    out.close()
