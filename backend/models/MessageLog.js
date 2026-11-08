const mongoose = require("mongoose");

const messageLogSchema = new mongoose.Schema(
  {
    channel: { type: String, enum: ["Notification", "Alert", "Broadcast"], required: true },
    recipient: { type: String, default: "All" },
    message: { type: String, required: true },
    status: { type: String, enum: ["Sent", "Queued", "Failed"], default: "Sent" },
  },
  { timestamps: true, collection: "message_logs" }
);

module.exports = mongoose.model("MessageLog", messageLogSchema);
