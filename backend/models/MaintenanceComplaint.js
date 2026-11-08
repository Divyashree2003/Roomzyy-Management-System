const mongoose = require("mongoose");

const maintenanceComplaintSchema = new mongoose.Schema(
  {
    tenantName: { type: String, required: true, trim: true },
    roomNumber: { type: String, required: true, trim: true },
    category: { type: String, required: true, trim: true },
    description: { type: String, required: true, trim: true },
    status: { type: String, enum: ["Open", "In Progress", "Resolved"], default: "Open" },
    resolvedAt: Date,
  },
  { timestamps: true }
);

module.exports = mongoose.model("MaintenanceComplaint", maintenanceComplaintSchema);
