const mongoose = require("mongoose");

const tenantSchema = new mongoose.Schema(
  {
    name: { type: String, required: true, trim: true },
    phone: { type: String, required: true, trim: true },
    email: { type: String, trim: true, lowercase: true },
    roomNumber: { type: String, required: true, trim: true },
    rentAmount: { type: Number, required: true, min: 0 },
    moveInDate: { type: Date, default: Date.now },
    status: { type: String, enum: ["Active", "Notice", "Left"], default: "Active" },
    guardianName: String,
    guardianPhone: String,
  },
  { timestamps: true }
);

module.exports = mongoose.model("Tenant", tenantSchema);
