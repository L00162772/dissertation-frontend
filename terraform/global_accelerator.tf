resource "aws_globalaccelerator_accelerator" "frontend_global_accelerator" {
  count           = var.aws_region == "us-east-1" ? 1 : 0
  name            = "frontend-global-accelerator"
  ip_address_type = "IPV4"
  enabled         = true

}

resource "aws_globalaccelerator_listener" "frontend_global_accelerator_listener" {
  count           = var.aws_region == "us-east-1" ? 1 : 0
  accelerator_arn = aws_globalaccelerator_accelerator.frontend_global_accelerator[1].id
  client_affinity = "SOURCE_IP"
  protocol        = "TCP"

  port_range {
    from_port = 80
    to_port   = 80
  }
}

resource "aws_globalaccelerator_endpoint_group" "frontend_global_accelerator_endpoint_group" {
  count        = var.aws_region != "us-east-1" ? 1 : 0
  listener_arn = aws_globalaccelerator_listener.frontend_global_accelerator_listener[1].id

  health_check_interval_seconds = 10
  health_check_path             = "/"
  threshold_count               = 3
  traffic_dial_percentage       = 100

  endpoint_configuration {
    endpoint_id = aws_lb.frontend_alb.arn
    weight      = 100
  }
}