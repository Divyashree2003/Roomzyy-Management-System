const mongoose = require("mongoose");

const alertSchema = new mongoose.Schema(
  {
    title: { type: String, required: true, trim: true },
    message: { type: String, required: true, trim: true },
    severity: { type: String, enum: ["Info", "Warning", "Emergency"], default: "Info" },
    isRead: { type: Boolean, default: false },
  },
  { timestamps: true, collection: "alerts" }
);

module.exports = mongoose.model("Alert", alertSchema);
