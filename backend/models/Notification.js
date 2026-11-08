const mongoose = require("mongoose");

const notificationSchema = new mongoose.Schema(
  {
    title: { type: String, required: true, trim: true },
    message: { type: String, required: true, trim: true },
    type: {
      type: String,
      enum: ["Rent Due", "Maintenance", "Visitor Alert", "Food Menu", "General"],
      default: "General",
    },
    isRead: { type: Boolean, default: false },
  },
  { timestamps: true, collection: "notifications" }
);

module.exports = mongoose.model("Notification", notificationSchema);
