import unittest
import os
import shutil
import filecmp
from socru.Socru  import Socru

test_modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(test_modules_dir, 'data','socru')

class TestOptions:
    def __init__(self, input_files, species, db_dir, min_bit_score,min_alignment_length, threads, output_file, not_circular, novel_profiles, new_fragments, max_bases_from_ends,top_blast_hits, output_plot_file, output_operon_directions_file ):
        self.input_files = input_files
        self.species = species
        self.db_dir = db_dir
        self.min_bit_score = min_bit_score
        self.min_alignment_length = min_alignment_length
        self.threads = threads
        self.output_file = output_file
        self.not_circular = not_circular
        self.novel_profiles = novel_profiles
        self.new_fragments = new_fragments
        self.max_bases_from_ends = max_bases_from_ends
        self.top_blast_hits = top_blast_hits
        self.output_plot_file = output_plot_file
        self.output_operon_directions_file = output_operon_directions_file
        self.verbose = False

class TestSocru(unittest.TestCase):

    def test_socru_valid(self):
        g = Socru(TestOptions([os.path.join(data_dir, 'test.fa')], 'Salmonella_enterica', None, 1000,1000,1, 'output_file', False, 'novel', 'newfrag.fa', None, 'blast', 'output_plot.png', 'directions'))
        g.run()
        self.assertTrue(os.path.exists('output_file'))
        self.assertTrue(os.path.exists('blast'))
        
        
        for file_name in ['blast', 'output_file', 'newfrag.fa', 'output_plot.png', 'novel', 'directions']:
            if os.path.exists(file_name):
                os.remove(file_name)
		
    def test_operon_wrapped_around_ends(self):
		# If there is no operon identified, then skip and dont throw an error
        g = Socru(TestOptions([os.path.join(data_dir, 'wrapped.fa')], 'Salmonella_enterica', None, 1000,1000,1, 'output_file', False, 'novel', 'newfrag.fa', None, 'blast', 'output_plot.png', 'directions'))
        g.run()
        self.assertTrue(os.path.exists('output_file'))
        self.assertTrue(os.path.exists('blast'))
        
        for file_name in ['blast', 'output_file', 'newfrag.fa', 'output_plot.png', 'novel', 'directions']:
            if os.path.exists(file_name):
                os.remove(file_name)
	
 