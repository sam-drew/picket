import picket

def test_ci():
	assert 5 == 5

def test_fence():
	new_fence = picket.Fence()
	try:
		new_fence.add_point((1, 1))
		new_fence.add_point((3, 1))
		new_fence.add_point((3, 3))
		new_fence.add_point((1, 3))
	except:
		assert 1 == 2
