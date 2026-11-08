const mongoose = require("mongoose");

const paymentSchema = new mongoose.Schema(
  {
    tenantName: { type: String, required: true, trim: true },
    roomNumber: { type: String, required: true, trim: true },
    amount: { type: Number, required: true, min: 0 },
    month: { type: String, required: true, trim: true },
    paidOn: { type: Date },
    dueDate: { type: Date, required: true },
    method: { type: String, enum: ["Cash", "UPI", "Card", "Bank"], default: "UPI" },
    status: { type: String, enum: ["Paid", "Pending", "Overdue"], default: "Pending" },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Payment", paymentSchema);
