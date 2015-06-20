import pymarc
from pymarc import Record, Field
from copy import deepcopy

############################################
# Read in a file of MARC records
############################################
my_records_in = pymarc.MARCReader(file('my_marc_recs_in.mrc'), to_unicode=True, force_utf8=True)

############################################
# Write out a file of MARC records
############################################
my_records_out = pymarc.MARCWriter(file('my_marc_recs_out.mrc', 'w'))


############################################
# Iterate through the input file of MARC records
############################################
rec_num = 1
for my_record in my_records_in:		# iterate through each of the records in the file
	print 'Record #: '+str(rec_num)
	my_orig_record = deepcopy(my_record)
	print_record = False
	
	
	############################################
	# DEMO 1 - Get 650 fields from MARC records using record.get_fields() function
# 	my_650s = my_record.get_fields('650')
# 	print 'List of field objects returned: '
# 	print my_650s
# 	
# 	print 'Individual fields: '
# 	for my_650 in my_650s:		# iterate through each of the 650 fields in the record
# 		print my_650
# 	print '----------------------------------------------'
	
	
	############################################
	# DEMO 2 - Add a 710 field to MARC records using record.add_ordered_field() function
# 	my_new_710 = Field(tag='710', indicators=['2',' '], subfields=['a', 'New York University.', 'b', 'Libraries.'])		# create the new field object
# 	my_record.add_ordered_field(my_new_710)			# add the new field object to the record
# 	print_record = True
	
	
	############################################
	# DEMO 3 - Analyze 65X fields, check for subfield $2, and modify MARC records	
# 	my_65Xs = my_record.get_fields('650', '651', '655')
# 	for my_65X in my_65Xs:		# iterate through each of the 65X fields in the record
# 		my_65X_2s = my_65X.get_subfields('2')
# 		if len(my_65X_2s) > 0:				# check if the 65X fields have a subfield $2
# 			my_record.remove_field(my_65X)
# 			print 'DELETED FIELD: ' + str(my_65X)
# 	print '----------------------------------------------'
	
	
	############################################
	#		HAND-ON EXERCISES
	############################################
	
	# EXERCISE 1 - Extract 1XX fields and print to the screen
	
	
	
	
	
	# EXERCISE 2 - Check if the record contains a 502 thesis note
	#	If it does, then add a 655 genre field for "Academic theses."
	
	
	
	
	

	
	############################################
	#		HAND-ON EXERCISES - ANSWERS
	############################################
	
	# EXERCISE 1 - Extract 1XX fields and print to the screen
# 	my_1XXs = my_record.get_fields('100', '110', '111', '130')
# 	for my_1XX in my_1XXs:
# 		print my_1XX
# 	print '----------------------------------------------'
	
	
	# EXERCISE 2 - Check if the record contains a 502 thesis note
	#	If it does, then add a 655 genre field for "Academic theses."
# 	my_502s = my_record.get_fields('502')
# 	if len(my_502s) > 0:
# 		my_new_655 = Field(tag='655', indicators=[' ', '0'], subfields=['a', 'Academic theses.'])
# 		my_record.add_ordered_field(my_new_655)
# 		print_record = True
	
	
	if print_record:
		print '******* Record BEFORE changes *******'
		print my_orig_record
		print '******* Record AFTER changes *******'
		print my_record
		print '----------------------------------------------'
	
	my_records_out.write(my_record)
	rec_num += 1

print 'Total records: ' + str(rec_num-1)
my_records_in.close()
my_records_out.close()
