import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const database = process.argv[2];

    try {
      const fields = await readDatabase(database);

      res.status(200);
      res.write('This is the list of our students\n');

      const sortedFields = Object.keys(fields).sort((a, b) => (
        a.toLowerCase().localeCompare(b.toLowerCase())
      ));

      sortedFields.forEach((field) => {
        res.write(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`,
        );
      });

      res.end();
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const fields = await readDatabase(database);
      res.status(200).send(`List: ${fields[major].join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
