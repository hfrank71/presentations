import pymarc
from pymarc import Record, Field

############################################
# Read in a file of MARC records
############################################
my_marc_recs_in = pymarc.MARCReader(file('my_marc_recs_in_1.mrc'), to_unicode=True, force_utf8=True) 


############################################
# Iterate through the input file of MARC records
############################################
for my_rec in my_marc_recs_in:
	
	##########################
	# Get fields out of the record using record.get_fields() function
	
	my_245s = my_rec.get_fields('245')	# there should only be *one* field in the list
#	print my_245s
	
	my_245 = my_245s[0]		# specify the list index position zero [0] to return the 1st field in the list
#	print my_245
	
	# OR
	
#	print my_rec['245']	# automatically only prints the first occurrence of the specified field
	
	
	# If there is more than one field in the returned list...
	my_650s = my_rec.get_fields('650')
	
	# iterate through the field objects in the list
	for my_650 in my_650s:
		print my_650['a']
#		print my_650
		pass
		
		# QUESTION: how to comment out the print command in a for loop if there isn't any other code there?
		#       that's why I put the do='stuff' line
	
#	print my_rec['650']		# automatically only prints the first occurrence of the specified field
	
	
	##########################
	# Get subfields out of the field using field.get_subfields() function
	
	my_650_subs = my_650.get_subfields('a', 'x')
#	print my_650_subs
	
	for my_650_sub in my_650_subs:
#		print my_650_sub
		pass

	
	print '----------------------'
