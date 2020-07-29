#!/usr/bin/env python3

from aws_cdk import core

from testlibcdk.testlibcdk_stack import TestlibcdkStack


app = core.App()
TestlibcdkStack(app, "testlibcdk")

app.synth()
