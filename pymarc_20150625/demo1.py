#*~*~*~*~*~*~*~  DRAFT ONLY   DRAFT ONLY   DRAFT ONLY   ~*~*~*~*~*~*~*
#*~*~*~*~*~*~*~  DEMO Code will be updated closer to the pre-conference date of June 25th   ~*~*~*~*~*~*~*
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
#		print my_650['a']
#		print my_650
		pass
		
		# QUESTION: how to comment out the print command in a for loop if there isn't any other code there?
		#       that's why I put the do='stuff' line
	
#	print my_rec['650']		# automatically only prints the first occurrence of the specified field
	
	
	##########################
	# Get subfields out of the field using field.get_subfields() function
#	my_650_subs = my_650.get_subfields()
	my_650_subs = my_650.get_subfields('a', 'x')
#	print my_650_subs
	
	for my_650_sub in my_650_subs:
#		print my_650_sub
		pass

#	print 'Before: '+ str(my_650)

#	my_650.delete_subfield('z')
	
#	my_650z_subs = my_650.get_subfields('z')
#	print my_650
#	for my_650z in my_650z_subs:
#		my_650.delete_subfield('z')
#		print my_650
	
#	my_650.add_subfield('2','local')
	
#	print 'After:  '+ str(my_650)
	
	my_new_700 = Field(tag='700', indicators=['1',' '])
	print my_new_700
	
	print my_new_700.indicator1
	my_new_700.indicator1 = '2'
	print my_new_700.indicator1
	print my_new_700
	my_new_700.add_subfield('a', 'Melville, Herman,')
	print my_new_700
	my_new_700.add_subfield('d', '1819-1891.')
	print my_new_700

	print '----------------------'



# PUTTING IT ALL TOGETHER
# 
# for my_record in my_marc_in:
# 	rec_245s = my_record.get_fields(‘245’)
# 	for rec_245 in rec_245s:
# 		rec_245.add_subfield(‘h’, ‘[electronic resource]’)
# 		rec_245a_subs = rec_245.get_subfields(‘a’)
# 		for rec_245a in rec_245a_subs:
# 			print rec_245a
# 	my_record.remove_field(‘006’)
# 	my_new_710 = Field(tag=‘710’, indicators=[‘1’, ‘ ’])
# 	my_new_710.add_subfield(‘a’, ‘Frank, Heidi’)
# 	my_record.add_field(my_new_710)
