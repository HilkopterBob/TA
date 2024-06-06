from Entities import Entity


from pytest import fixture


@fixture
def entity_npc():
    return Entity(
        "TestNPC",
        100,
        0,
        100,
        ["NPCItem"],
        None,
        ["NPCGoodEffect"],
        ["NPCBadEffect"],
        ["NPCEvilEffect"],
        "NPCLocationLevel",
        18,
        True,
        None,
        None,
        None,
        None,
        10,
        False,
        0,
        800,
    )


def test_entity_init(entity_npc: Entity):
    assert entity_npc.name == "TestNPC"
    assert entity_npc.health == 100
    assert entity_npc.wealth == 0
    assert entity_npc.xp == 100
    assert entity_npc.inv == ["NPCItem"]
    assert entity_npc.ptype is None
    assert entity_npc.geffects == ["NPCGoodEffect"]
    assert entity_npc.beffects == ["NPCBadEffect"]
    assert entity_npc.eeffects == ["NPCEvilEffect"]
    assert entity_npc.location == "NPCLocationLevel"
    assert entity_npc.level == 18
    assert entity_npc.allowdamage == True
    assert entity_npc.slots is None
    assert entity_npc.attributes is None
    assert entity_npc.loottable is None
    assert entity_npc.ai is None
    assert entity_npc.spd == 10
    assert entity_npc.isPlayer == False
    assert entity_npc.Team == 0
    assert entity_npc.maxHealth == 800
