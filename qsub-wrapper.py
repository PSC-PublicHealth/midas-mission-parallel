import sh
import os
import concurrent.futures


base_dir = '/mnt/beegfs1/data/synthetic_ecosystems/rti_synthetic_populations/United_States_2010_ver1'

populations = ['2010_ver1_48021','2010_ver1_48023','2010_ver1_48025','2010_ver1_48027']

# The '-I -x' options when combined cause the qsub command to run in the foreground
qsub = sh.qsub.bake('-I','-x')

# First do a single example
pop_path = '{}/{}/{}_synth_people.txt'.format(base_dir,populations[0],populations[0])

# This is the full output from qsub
cmd_result_string = qsub('-v','POP={}'.format(pop_path), os.path.join(os.getcwd(), 'example.bash'))
print(cmd_result_string)

# For this example, need to extract the output of interest from the output string
res = cmd_result_string.splitlines()
print(int(res[3].split()[0]))


# now show how this can be used in parallel

def get_lines_in_file(pop):
    pop_path = '{}/{}/{}_synth_people.txt'.format(base_dir,pop,pop)
    cmd_result_string = qsub('-v','POP={}'.format(pop_path), os.path.join(os.getcwd(), 'example.bash'))
    res = cmd_result_string.splitlines()
    return int(res[3].split()[0])


with concurrent.futures.ProcessPoolExecutor() as executor:
    for pop, res in zip(populations, executor.map(get_lines_in_file, populations)):
        print('%s has %d lines' % (pop,res))

