const MaintenanceComplaint = require("../models/MaintenanceComplaint");
const controller = require("./crudController")(MaintenanceComplaint);

controller.resolve = async (req, res) => {
  try {
    const complaint = await MaintenanceComplaint.findByIdAndUpdate(
      req.params.id,
      { status: "Resolved", resolvedAt: new Date() },
      { new: true }
    );

    if (!complaint) return res.status(404).json({ message: "Complaint not found" });
    res.json(complaint);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

module.exports = controller;
