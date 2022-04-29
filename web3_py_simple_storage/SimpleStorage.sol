// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 public favoriteNumber = 5;
    // bool favoriteBool = false;
    // string favoriteString = 'String';
    // int256 favoriteInt = -5;
    // address favoriteAddress = 0xE995b6994e5D9FEE2afF0548e51e646f983489D2;
    // bytes32 favoriteBytes = 'Calf';

    struct People{
        uint256 myNumber;
        string name;

    }

    People[] public people;
    mapping(string => uint256) public _ndiIgbo;

    //People public people = People({myNumber:3000, name:'Ugwumsinachi'});

    //This function essentially changes the value of the variable above.
    function store(uint256 _favorite) public {
        favoriteNumber = _favorite;
    }

    function retrieve() view public returns(uint256){
        return favoriteNumber;
    }

    function addPerson(string memory newName, uint256 newNumber) public{
        people.push(People({myNumber:newNumber,name:newName})); 
        _ndiIgbo[newName] = newNumber;
    }
}