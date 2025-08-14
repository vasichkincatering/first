const express = require('express');
const Project = require('./models/project');
const Menu = require('./models/menu');
const calculateResources = require('./services/calculateResources');

const app = express();
app.use(express.json());
app.use(express.static('public'));

const projects = new Map();

// Create a new project
app.post('/projects', (req, res) => {
  const { client, startDate, endDate, status } = req.body;
  const id = Date.now().toString();
  const project = new Project({ id, client, startDate, endDate, status });
  projects.set(id, project);
  res.json(project);
});

// Get menu for a project
app.get('/projects/:id/menu', (req, res) => {
  const project = projects.get(req.params.id);
  if (!project) return res.status(404).send('Project not found');
  res.json(project.menu || {});
});

// Save menu and calculate resources
app.post('/projects/:id/menu', (req, res) => {
  const project = projects.get(req.params.id);
  if (!project) return res.status(404).send('Project not found');
  const menu = new Menu({ items: req.body.items });
  project.menu = menu;
  project.resources = calculateResources(menu);
  res.json({ menu: project.menu, resources: project.resources });
});

// View calculated resources
app.get('/projects/:id/resources', (req, res) => {
  const project = projects.get(req.params.id);
  if (!project) return res.status(404).send('Project not found');
  res.json(project.resources);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));
