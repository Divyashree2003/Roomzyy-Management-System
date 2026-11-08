const mongoose = require("mongoose");

const visitorSchema = new mongoose.Schema(
  {
    visitorName: { type: String, required: true, trim: true },
    tenantName: { type: String, required: true, trim: true },
    roomNumber: { type: String, required: true, trim: true },
    phone: { type: String, required: true, trim: true },
    purpose: { type: String, required: true, trim: true },
    entryTime: { type: Date, default: Date.now },
    exitTime: Date,
    status: { type: String, enum: ["Inside", "Exited"], default: "Inside" },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Visitor", visitorSchema);
