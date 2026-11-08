const express = require("express");
const controller = require("../controllers/notificationController");
const auth = require("../middleware/authMiddleware");

const router = express.Router();

router.use(auth);
router.get("/", controller.list);
router.post("/", controller.create);
router.post("/alerts", controller.createAlert);
router.patch("/:kind/:id/read", controller.markRead);

module.exports = router;
