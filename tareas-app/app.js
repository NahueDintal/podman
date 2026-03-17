const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());

// Conectar a MongoDB
const mongoUrl = process.env.MONGO_URL || 'mongodb://localhost:27017/tareas';
mongoose.connect(mongoUrl);

// Esquema de tarea
const Tarea = mongoose.model('Tarea', {
  texto: String,
  completada: { type: Boolean, default: false }
});

// Rutas
app.get('/tareas', async (req, res) => {
  const tareas = await Tarea.find();
  res.json(tareas);
});

app.post('/tareas', async (req, res) => {
  const tarea = new Tarea(req.body);
  await tarea.save();
  res.status(201).json(tarea);
});

app.listen(3000, () => {
  console.log('Servidor escuchando en puerto 3000');
});
