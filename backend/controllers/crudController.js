const createCrudController = (Model) => ({
  list: async (req, res) => {
    try {
      const items = await Model.find().sort({ createdAt: -1 });
      res.json(items);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },

  create: async (req, res) => {
    try {
      const item = await Model.create(req.body);
      res.status(201).json(item);
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
  },

  update: async (req, res) => {
    try {
      const item = await Model.findByIdAndUpdate(req.params.id, req.body, {
        new: true,
        runValidators: true,
      });

      if (!item) return res.status(404).json({ message: "Record not found" });
      res.json(item);
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
  },

  remove: async (req, res) => {
    try {
      const item = await Model.findByIdAndDelete(req.params.id);

      if (!item) return res.status(404).json({ message: "Record not found" });
      res.json({ message: "Record deleted" });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
});

module.exports = createCrudController;
