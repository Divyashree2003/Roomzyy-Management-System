const Visitor = require("../models/Visitor");
const controller = require("./crudController")(Visitor);

controller.exit = async (req, res) => {
  try {
    const visitor = await Visitor.findByIdAndUpdate(
      req.params.id,
      { status: "Exited", exitTime: new Date() },
      { new: true }
    );

    if (!visitor) return res.status(404).json({ message: "Visitor not found" });
    res.json(visitor);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

module.exports = controller;
