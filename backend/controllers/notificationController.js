const Notification = require("../models/Notification");
const Alert = require("../models/Alert");
const MessageLog = require("../models/MessageLog");

exports.list = async (req, res) => {
  try {
    const [notifications, alerts, logs] = await Promise.all([
      Notification.find().sort({ createdAt: -1 }),
      Alert.find().sort({ createdAt: -1 }),
      MessageLog.find().sort({ createdAt: -1 }).limit(25),
    ]);

    res.json({ notifications, alerts, logs });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.create = async (req, res) => {
  try {
    const notification = await Notification.create(req.body);
    await MessageLog.create({
      channel: "Notification",
      message: `${notification.type}: ${notification.message}`,
      status: "Sent",
    });

    res.status(201).json(notification);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

exports.createAlert = async (req, res) => {
  try {
    const alert = await Alert.create(req.body);
    await MessageLog.create({
      channel: "Alert",
      message: `${alert.severity}: ${alert.message}`,
      status: "Sent",
    });

    res.status(201).json(alert);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

exports.markRead = async (req, res) => {
  try {
    const Model = req.params.kind === "alerts" ? Alert : Notification;
    const item = await Model.findByIdAndUpdate(
      req.params.id,
      { isRead: true },
      { new: true }
    );

    if (!item) return res.status(404).json({ message: "Record not found" });
    res.json(item);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
