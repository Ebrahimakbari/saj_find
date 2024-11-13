# Sajj (Rhymed Prose) Detection Algorithm

This Python script detects instances of Sajj (rhymed prose) in a given text. Sajj is an Arabic-derived literary device used in Persian literature, where pairs of words or phrases at the end of sentences rhyme or have similar endings.

## Features

- Splits the input text into sentences
- Identifies pairs of sentences where the last words or second-to-last words rhyme
- Outputs the detected Sajj pairs with the corresponding sentences
- Can be used to process an entire file and write the results to an output file

## Usage

1. Make sure you have Python installed on your system.
2. Save the Python script (e.g., `sajj_detection.py`) to a directory.
3. Run the script with the following command:

   ```
   python sajj_detection.py <input_file> <output_file>
   ```

   Replace `<input_file>` with the path to the file you want to process, and `<output_file>` with the desired output file path.

4. The script will create the output file and write the detected Sajj pairs to it.


## Customization

You can customize the algorithm by modifying the following functions:

- `split_sentences(text)`: Adjust the sentence splitting logic.
- `check_sajj(word1, word2)`: Modify the criteria for determining if two words have a Sajj relationship.
- `find_sajj_in_sentence_pair(sentence1, sentence2)`: Customize the logic for detecting Sajj pairs within a pair of sentences.

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the project's GitHub repository.
