const express = require("express");
const controller = require("../controllers/visitorController");
const auth = require("../middleware/authMiddleware");

const router = express.Router();

router.use(auth);
router.get("/", controller.list);
router.post("/", controller.create);
router.put("/:id", controller.update);
router.patch("/:id/exit", controller.exit);
router.delete("/:id", controller.remove);

module.exports = router;
