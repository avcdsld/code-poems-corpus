class LookCloser
{
  public: bool broken, purpose, ornament;
  public: LookCloser (
      bool broken,
      bool purpose,
      bool ornament)
  {
    this->broken =
      (broken ^ purpose) &&
      (purpose || ornament);
    this->purpose =
      !purpose ||
      (broken && ornament);
    this->ornament =
      (purpose ^ ornament) &&
      !(broken && ornament);
  }
};
