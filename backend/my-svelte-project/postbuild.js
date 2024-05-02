import fs from 'fs-extra';

const sourcePath = 'dist';
const destinationPath = '../backend/frontend/static/build';

fs.copySync(sourcePath, destinationPath, { overwrite: true });
console.log('Build files copied to Django static directory.');