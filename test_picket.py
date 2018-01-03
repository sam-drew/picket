import picket

def test_addpoints():
	new_fence = picket.Fence()
	try:
		new_fence.add_point((1, 1))
		new_fence.add_point((3, 1))
		new_fence.add_point((3, 3))
		new_fence.add_point((1, 3))
		assert new_fence.points[0] == (1, 1)
		assert new_fence.points[1] == (3, 1)
		assert new_fence.points[2] == (3, 3)
		assert new_fence.points[3] == (1, 3)
	except:
		assert 1 == 2

def test_list_points():
	my_fence = picket.Fence()

	my_fence.add_point((1, 1))
	my_fence.add_point((3, 1))
	my_fence.add_point((3, 3))
	my_fence.add_point((1, 3))

	assert my_fence.list_points() == [(1, 1), (3, 1), (3, 3), (1, 3)]
