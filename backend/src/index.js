const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Backend çalışıyor!' });
});

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`Backend ${PORT} portunda çalışıyor.`));
