import os

# Dosya yolu
output_file = "backend/src/routes/events.js"

# Klasörleri oluştur (varsa atla)
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Mock Node.js kodu (API çağrısı yapmadan workflow testi için)
code = """
// Mock Node.js route for nearby events
const express = require('express');
const router = express.Router();

router.get('/events', (req, res) => {
    res.json({
        message: 'This is a mock response for testing workflow.',
        events: [
            {id: 1, name: 'Concert in Park', date: '2025-11-25'},
            {id: 2, name: 'Art Exhibition', date: '2025-11-27'}
        ]
    });
});

module.exports = router;
"""

# Dosyaya yaz
with open(output_file, "w") as f:
    f.write(code)

print(f"Mock code generated at {output_file}")
