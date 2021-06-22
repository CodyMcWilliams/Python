DuplicateLineFinder was created to find duplicate IP addresses across multiple files.

DuplicateLineFinder can be run from the command line or as an executable.

If run as an executable it will compare all files in the same directory except those ending in .exe.

If run in the command line with less than two inputs it will run as if it was an executable.

Example output using GUIDS:
$>
	Comparing all files in the parent directory...

	Instance of '7ef6b0a7-39b4-4493-ba07-28ad1c8bb331' found in:
        	sampleInput1.txt on the following lines [2]

        	sampleInput2.txt on the following lines [1]

        	sampleInput3.txt on the following lines [3]

	Instance of 'b94fe13c-1bca-4396-a5cf-108bbe336024' found in:
        	sampleInput1.txt on the following lines [4]

        	sampleInput2.txt on the following lines [3]

        	sampleInput3.txt on the following lines [4]

	Instance of 'de1498d7-80ac-496a-918a-73f72bcfb1c7' found in:
       		sampleInput2.txt on the following lines [2]

        	sampleInput3.txt on the following lines [5]


	Press enter to exit.
