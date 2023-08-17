# Create a VPC
resource "aws_vpc" "Terra_Vpc" {
  cidr_block = "10.0.0.0/16"
}

# Create a Subnet
resource "aws_subnet" "Terra_subnet" {
  vpc_id     = aws_vpc.Terra_Vpc.id
  cidr_block = "10.0.0.0/24"
}

# Creating the Internet Gateway
resource "aws_internet_gateway" "Terra_gw" {
  vpc_id = aws_vpc.Terra_Vpc.id
}

# Creating the Route Table
resource "aws_route_table" "Terra_rt" {
  vpc_id = aws_vpc.Terra_Vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.Terra_gw.id
  }
}

#creating association on my subnet on the created IGW
resource "aws_route_table_association" "Terra_association" {
  subnet_id      = aws_subnet.Terra_subnet.id
  route_table_id = aws_route_table.Terra_rt.id
}


# Creating a security group to allow http and https and ssh
resource "aws_security_group" "sprints_sg" {
  name        = "allow_http"
  description = "Allow http inbound traffic"
  vpc_id      = aws_vpc.Terra_Vpc.id
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
  tags = {
    Name = "Sprints"
  }
}
# Creating the instance i will connect
resource "aws_instance" "Terra_instance" {
  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.Terra_subnet.id
  associate_public_ip_address = true
  security_groups = [aws_security_group.sprints_sg.id]


      user_data = <<EOF
#! /bin/bash
sudo apt-get update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
EOF
}