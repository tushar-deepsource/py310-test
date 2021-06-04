resource "aws_instance" "webber" {
  ami                  = "ami-b73b63a0"
  instance_type        = "t1.micro"
  iam_instance_profile = "app-service"

  tags {
    Name = "HeyWorld"
  }
}

resource "aws_db_instance" "default" {
  allocated_storage    = 10
  engine               = "mysql"
  engine_version       = "5.6.17"
  instance_class       = "db.t1.micro"
  name                 = "mydb"
  username             = "foo"
  password             = "bar"
  db_subnet_group_name = "my_database_subnet_group"
  parameter_group_name = "default.mysql5.6"
}
