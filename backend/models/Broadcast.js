const mongoose = require("mongoose");

const broadcastSchema = new mongoose.Schema(
  {
    title: { type: String, required: true, trim: true },
    message: { type: String, required: true, trim: true },
    audience: { type: String, enum: ["All", "Staff", "Tenants"], default: "All" },
    priority: { type: String, enum: ["Normal", "Emergency"], default: "Normal" },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Broadcast", broadcastSchema);
