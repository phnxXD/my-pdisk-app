const express = require('express');
const axios = require('axios');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.static('public'));

app.get('/api/folder/list', async (req, res) => {
  try {
    const folderId = req.query.fld_id;
    const apiKey = req.query.key;
    const apiUrl = `https://pdisk.pro/api/folder/list?fld_id=${folderId}&key=${apiKey}`;

    const response = await axios.get(apiUrl);

    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
